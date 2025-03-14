/** @odoo-module */

import { registry } from "@web/core/registry";
import { standardWidgetProps } from "@web/views/widgets/standard_widget_props";

import { Component } from "@odoo/owl";

class CenterTagWidget extends Component {
    static template = "ekika_widgets.CenterTag";
    static props = {
        ...standardWidgetProps,
        title: { type: String},
        bg_class: { type: String, optional: true },
    };
    static defaultProps = {
        bg_class: "text-bg-success"
    };

    get classes() {
        let classes = this.props.bg_class + " center_inner_block";
        return classes;
    }

}

export const centerTagWidget = {
    component: CenterTagWidget,
    extractProps: ({ attrs }) => {
        return {
            title: attrs.title,
            bg_class: attrs.bg_class,
        };
    },
};

registry.category("view_widgets").add("center_tag", centerTagWidget);
