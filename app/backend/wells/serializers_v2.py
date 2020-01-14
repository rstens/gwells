"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import logging

from rest_framework import serializers
from wells.models import Well


logger = logging.getLogger(__name__)


class WellLocationSerializerV2(serializers.ModelSerializer):
    """ serializes well locations """

    class Meta:
        model = Well
        fields = ("well_tag_number", "identification_plate_number",
                  "latitude", "longitude", "street_address", "city", "ems")