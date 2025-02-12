/** @odoo-module */

import {patch} from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype, {
	shouldDownloadInvoice() {
		return this.pos.config.auto_download_invoice_after_validate_order
		&& super.shouldDownloadInvoice();
	},
});
