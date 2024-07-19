from odoo import models, api, fields
from datetime import timedelta

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def get_worked_day_lines(self, contracts, date_from, date_to=None):
        res = super(HrPayslip, self).get_worked_day_lines(contracts, date_from, date_to)

        # Adjust leave days to include sandwich logic
        for line in res:
            if line['code'] == 'Unpaid':  # Adjust the code to match your leave code
                employee_leaves = self.env['hr.leave'].search([
                    ('employee_id', '=', self.employee_id.id),
                    ('state', '=', 'validate'),
                    ('date_from', '>=', self.date_from),
                    ('date_to', '<=', self.date_to)
                ])

                total_sandwich_days = 0
                for leave in employee_leaves:
                    start_date = fields.Date.from_string(leave.date_from)
                    end_date = fields.Date.from_string(leave.date_to)
                    delta = (end_date - start_date).days + 1  # Include the end date
                    sandwich_days = self._calculate_sandwich_days(start_date, end_date)
                    total_sandwich_days +=  sandwich_days

                # Update the leave days with sandwich days
                line['number_of_days'] = delta

                

        return res

    def _calculate_sandwich_days(self, start_date, end_date):
        sandwich_days = 0

        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() in (5, 6):  # Saturday or Sunday
                sandwich_days += 1
            current_date += timedelta(days=1)

        return sandwich_days
