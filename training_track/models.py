# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import fields, models


class EventTrack(models.Model):
    """Expand event tracks with training duration types.

    This is used to calculate how many hours of each type have been fulfilled.
    """

    _inherit = "event.track"

    duration_type_id = fields.Many2one(
        "training.duration_type",
        "Training hour type",
        help="Training hour type of this track, if it belongs to a training "
             "group.")
