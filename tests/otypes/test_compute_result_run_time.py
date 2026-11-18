# Copyright (C) 2026 Rainer Garus
#
# This file is part of the ooresults Python package, a software to
# compute results of orienteering events.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from datetime import datetime
from datetime import timedelta
from datetime import timezone

import pytest

from ooresults.model.build_results import build_results
from ooresults.model.build_results import build_total_results
from ooresults.otypes.class_params import ClassParams
from ooresults.otypes.class_type import ClassInfoType
from ooresults.otypes.entry_type import EntryType
from ooresults.otypes.entry_type import RankedEntryType
from ooresults.otypes.result_type import PersonRaceResult
from ooresults.otypes.result_type import ResultStatus
from ooresults.otypes.result_type import SplitTime
from ooresults.otypes.result_type import SpStatus
from ooresults.otypes.series_type import Settings


START = datetime(2015, 1, 1, 11, 0, 0, tzinfo=timezone.utc)


def class_info(params: ClassParams) -> ClassInfoType:
    return ClassInfoType(
        id=1,
        name="Bahn A",
        short_name=None,
        course_id=None,
        course_name=None,
        course_length=None,
        course_climb=None,
        number_of_controls=None,
        params=params,
    )


def result_with_finish(finish: datetime) -> PersonRaceResult:
    return PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_finish_time=finish,
        split_times=[
            SplitTime(
                control_code="101",
                punch_time=START - timedelta(minutes=20),
                status=SpStatus.ADDITIONAL,
            ),
        ],
    )


@pytest.mark.parametrize("otype", ["standard", "net", "score"])
@pytest.mark.parametrize("seconds", [-600, 0])
def test_run_time_less_or_equal_zero_is_invalid(otype: str, seconds: int) -> None:
    result = result_with_finish(finish=START + timedelta(seconds=seconds))
    params = ClassParams(otype=otype, time_limit=3600)

    result.compute_result(controls=["101"], class_params=params, start_time=START)

    assert result.time is None
    assert result.status == ResultStatus.MISSING_PUNCH
    if otype == "score":
        assert result.extensions["score"] is None


def test_run_time_greater_zero_is_valid() -> None:
    result = result_with_finish(finish=START + timedelta(seconds=1))
    result.split_times[0].punch_time = START + timedelta(microseconds=500000)

    result.compute_result(
        controls=["101"], class_params=ClassParams(), start_time=START
    )

    assert result.time == 1
    assert result.status == ResultStatus.OK


def test_finish_before_start_gets_no_rank() -> None:
    params = ClassParams()
    entries = []
    for i, finish in enumerate(
        [START - timedelta(minutes=10), START + timedelta(minutes=30)]
    ):
        result = result_with_finish(finish=finish)
        result.split_times[0].punch_time = START + timedelta(minutes=1)
        result.compute_result(controls=["101"], class_params=params, start_time=START)
        entries.append(
            EntryType(
                id=i,
                event_id=1,
                competitor_id=i,
                first_name="First",
                last_name=f"Last {i}",
                class_name="Bahn A",
                result=result,
            )
        )

    [(_, ranked)] = build_results(class_infos=[class_info(params)], entries=entries)

    assert ranked[0].entry.last_name == "Last 1"
    assert ranked[0].rank == 1
    assert ranked[1].entry.last_name == "Last 0"
    assert ranked[1].rank is None


def test_series_with_run_time_zero_does_not_raise() -> None:
    entry = EntryType(
        id=1,
        event_id=1,
        competitor_id=1,
        first_name="First",
        last_name="Last",
        class_name="Bahn A",
        result=PersonRaceResult(status=ResultStatus.OK, time=0),
    )
    results = [[(class_info(ClassParams()), [RankedEntryType(entry=entry, rank=1)])]]

    build_total_results(settings=Settings(), list_of_results=results)
