from odoo import models, fields, api
from datetime import timedelta

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    @api.model
    def create(self, vals):
        leave = super(HrLeave, self).create(vals)
        leave._adjust_sandwich_leaves()
        return leave

    def write(self, vals):
        # Call super() without calling _adjust_sandwich_leaves to avoid recursion
        res = super(HrLeave, self).write(vals)
        if 'date_from' in vals or 'date_to' in vals:
            # Check if date_from or date_to is in the vals dict to avoid unnecessary calls
            for leave in self:
                leave._adjust_sandwich_leaves()
        return res

    def _adjust_sandwich_leaves(self):
        for leave in self:
            start_date = fields.Date.from_string(leave.date_from)
            end_date = fields.Date.from_string(leave.date_to)

            # Calculate the number of days between start and end dates
            delta = (end_date - start_date).days + 1  # Include the end date
            sandwich_days = self._calculate_sandwich_days(start_date, end_date)

            # Update the leave record without calling write() again
            leave.number_of_days = delta

    def _calculate_sandwich_days(self, start_date, end_date):
        sandwich_days = 0
       
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() in (5, 6):  # Saturday or Sunday
                sandwich_days += 1
            current_date += timedelta(days=1)

        return sandwich_days
