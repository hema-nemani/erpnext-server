!function(){"use strict";$(document).on("toolbar_setup",function(){frappe.versions||frappe.call({method:"frappe.utils.change_log.get_versions",callback:function(e){frappe.versions=e.message,$("<li><a href='https://erpnext.com/support' target='_blank' rel='noopener noreferrer'>"+__("Need Support?")+"</a></li>").insertAfter($("#toolbar-help").find("li:first"))}})}),$(window).bind("hashchange",function(){"modules/Settings"===frappe.get_route_str()&&frappe.db.get_doc("Helper System Settings").then(function(e){"unread"===e.email_message_status&&(frappe.msgprint({title:__("Email Notice"),message:__("<h5>For DigitalOcean Users</h5><h5>New accounts may not have SMTP access enabled until they are verified and have payment history. In this case, your ERPNext instance may not be able to push emails out and will likely be stuck in the <i>Email Queue</i></h5>"),wide:!0}).keep_open=!0,frappe.db.set_value("Helper System Settings","Helper System Settings","email_message_status","read"))})})}();
//# sourceMappingURL=erpnext_helper.js.map