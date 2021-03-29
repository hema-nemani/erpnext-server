// erpnext.setup.slides_settings.push(...[
// 	{
// 		// Domain
// 		name: 'Setup SSL',
// 		title: __('Do you have a Domain?'),
// 		fields: [
// 			{
// 				fieldname: 'domain_name',
// 				label: __('Domain Name'),
// 				fieldtype: 'Data'
// 			},
// 		],
// 		// help: __('Select the nature of your business.'),
// 		validate: function () {
// 			if (this.values.domains.length === 0) {
// 				frappe.msgprint(__("Please select at least one domain."));
// 				return false;
// 			}
// 			frappe.setup.domains = this.values.domains;
// 			return true;
// 		}
// 	}
// ]);