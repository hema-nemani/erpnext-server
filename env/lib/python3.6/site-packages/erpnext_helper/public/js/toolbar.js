// Copyright (c) 2019, Frappe Technologies Pvt. Ltd.
// For license information, please see license.txt

$(document).on("toolbar_setup", function() {
    if(!frappe.versions) {
        frappe.call({
            method: "frappe.utils.change_log.get_versions",
            callback: function(r) {
                frappe.versions = r.message;
                setup_toolbar();
            }
        });
    }

    function setup_toolbar() {
        $(
            "<li><a href='https://erpnext.com/support' target='_blank' rel='noopener noreferrer'>"
            + __("Need Support?")
            + "</a></li>"
        ).insertAfter($("#toolbar-help").find("li:first"));
    }
});
