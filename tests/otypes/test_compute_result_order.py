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

from ooresults.otypes.class_params import ClassParams
from ooresults.otypes.result_type import PersonRaceResult
from ooresults.otypes.result_type import ResultStatus
from ooresults.otypes.result_type import SplitTime
from ooresults.otypes.result_type import SpStatus


START = datetime(2015, 1, 1, 11, 0, 0, tzinfo=timezone.utc)
FINISH = START + timedelta(minutes=30)
CONTROLS = ["101", "102", "103", "104", "105"]


def result_with_punches(codes: list[str]) -> PersonRaceResult:
    return PersonRaceResult(
        status=ResultStatus.INACTIVE,
        punched_start_time=START,
        punched_finish_time=FINISH,
        split_times=[
            SplitTime(
                control_code=code,
                punch_time=START + timedelta(minutes=i + 1),
                status=SpStatus.ADDITIONAL,
            )
            for i, code in enumerate(codes)
        ],
    )


def statuses(result: PersonRaceResult) -> list[tuple[str, SpStatus | None]]:
    return [(s.control_code, s.status) for s in result.split_times]


def test_control_punched_at_the_end_is_one_missing_control() -> None:
    result = result_with_punches(["102", "103", "104", "105", "101"])
    params = ClassParams(otype="standard", penalty_controls=60)

    result.compute_result(controls=CONTROLS, class_params=params)

    assert result.status == ResultStatus.OK
    assert result.extensions["running_time"] == 1800
    assert result.extensions["penalties_controls"] == 60
    assert result.time == 1860
    assert statuses(result) == [
        ("101", SpStatus.MISSING),
        ("102", SpStatus.OK),
        ("103", SpStatus.OK),
        ("104", SpStatus.OK),
        ("105", SpStatus.OK),
        ("101", SpStatus.ADDITIONAL),
    ]
    assert [s.time for s in result.split_times if s.status == SpStatus.OK] == [
        60,
        120,
        180,
        240,
    ]


def test_control_punched_at_the_end_without_penalty_rule() -> None:
    result = result_with_punches(["102", "103", "104", "105", "101"])

    result.compute_result(controls=CONTROLS, class_params=ClassParams())

    assert result.status == ResultStatus.MISSING_PUNCH
    assert [
        s.control_code for s in result.split_times if s.status == SpStatus.MISSING
    ] == ["101"]


def test_swapped_controls_are_one_missing_control() -> None:
    result = result_with_punches(["101", "103", "102", "104", "105"])
    params = ClassParams(otype="standard", penalty_controls=60)

    result.compute_result(controls=CONTROLS, class_params=params)

    assert result.extensions["penalties_controls"] == 60
    assert statuses(result) == [
        ("101", SpStatus.OK),
        ("103", SpStatus.ADDITIONAL),
        ("102", SpStatus.OK),
        ("103", SpStatus.MISSING),
        ("104", SpStatus.OK),
        ("105", SpStatus.OK),
    ]


def test_repeated_punch_uses_the_first_punch() -> None:
    result = result_with_punches(["101", "101", "102", "103", "104", "105"])

    result.compute_result(controls=CONTROLS, class_params=ClassParams())

    assert result.status == ResultStatus.OK
    assert statuses(result)[:2] == [
        ("101", SpStatus.OK),
        ("101", SpStatus.ADDITIONAL),
    ]
