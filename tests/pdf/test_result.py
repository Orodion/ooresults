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


import io
from datetime import date

import pypdf
import pytest

from ooresults.otypes.class_params import ClassParams
from ooresults.otypes.class_type import ClassInfoType
from ooresults.otypes.entry_type import EntryType
from ooresults.otypes.entry_type import RankedEntryType
from ooresults.otypes.event_type import EventType
from ooresults.otypes.result_type import PersonRaceResult
from ooresults.otypes.result_type import ResultStatus
from ooresults.pdf.result import create_pdf


EVENT = EventType(
    id=1,
    name="1. O-Cup 2020",
    date=date(year=2020, month=2, day=9),
    key=None,
    publish=False,
    series=None,
    fields=[],
)


def class_results(params: ClassParams) -> list:
    class_info = ClassInfoType(
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
    entry = EntryType(
        id=1,
        event_id=1,
        competitor_id=1,
        first_name="Angela",
        last_name="Merkel",
        year=1957,
        class_id=1,
        class_name="Bahn A",
        club_name="OL Bundestag mit einem sehr langen Vereinsnamen",
        result=PersonRaceResult(status=ResultStatus.OK, time=1234),
    )
    return [(class_info, [RankedEntryType(entry=entry, rank=1, time_behind=0)])]


@pytest.mark.parametrize("landscape", [True, False])
@pytest.mark.parametrize(
    "params",
    [
        ClassParams(),
        ClassParams(otype="score", apply_handicap_rule=True),
        ClassParams(
            penalty_controls=60,
            penalty_overtime=60,
            apply_handicap_rule=True,
        ),
    ],
)
def test_create_pdf_with_wide_classes(params: ClassParams, landscape: bool) -> None:
    content = create_pdf(
        event=EVENT,
        results=class_results(params=params),
        landscape=landscape,
    )

    reader = pypdf.PdfReader(io.BytesIO(content))
    text = reader.pages[0].extract_text()
    assert "Bahn A" in text
    assert "Merkel" in text
    assert "Verein" in text
