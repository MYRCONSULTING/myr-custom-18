/** @odoo-module **/
import { registry } from "@web/core/registry";
import { RadioField } from "@web/views/fields/radio/radio_field";

class RadioDetailField extends RadioField{
    setup(){
        super.setup()
    }

    specificText(key){
        let value = this.props.radio_text[`${key}_text`]
        return value
    }

    specificIcon(key){
        let value = this.props.radio_icon[`${key}_icon`]
        return value
    }
}

RadioDetailField.template = "ekika_utils.RadioDetailField";

RadioDetailField.props = {
    ...RadioField.props,
    radio_text: { type: Object, optional: true },
    radio_icon: { type: Object, optional: true },
};
RadioDetailField.defaultProps = {
    ...RadioField.defaultProps,
    radio_text: null,
    radio_icon: null,
};

function addValuesWithKeyEndingWith(object, keyPrefix) {
    let values = {};
        for (const prop in object) {
            if (prop.endsWith(keyPrefix)) {
            values[prop] = object[prop]
            }
        }
    return values;
  }

export const radioDetailField = {
    component: RadioDetailField,
    supportedTypes: ["selection"],
    extractProps: ({ attrs }) => ({
        orientation: "vertical",
        radio_text: addValuesWithKeyEndingWith(attrs, "text"),
        radio_icon: addValuesWithKeyEndingWith(attrs, "icon"),
    }),
};
registry.category("fields").add("radio_detail", radioDetailField);
