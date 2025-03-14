/** @odoo-module **/

import { Component} from "@odoo/owl";
import { registry } from "@web/core/registry";

export class RestJsonSwaggerDocAction extends Component {
    static components = { };
    static props = ["*"];
    setup(){
        this.apiBaseEndpoint = this.props.action.context.active_id
    }
}

RestJsonSwaggerDocAction.template = "easy_restjson.RestJsonSwaggerDocViewClient"


registry
    .category("actions")
    .add("easy_restjson.restjson_swagger_doc_action", RestJsonSwaggerDocAction);
