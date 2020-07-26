import _ from "lodash";
import axios from "axios";

export function calcCartGoodId(good) {
	if (good.specifications.length > 0) {
		return good.goodsId + '_' + good.product_id + '_' + good.specifications.join('_');
	}
	return good.goodsId + '_' + good.product_id;
}


export function printOrder(order) {

	let orderdata = {}
	orderdata.orderNo = order.order_no;
	orderdata.total = order.fee;
	orderdata.status = order.status;
	orderdata.orderTime = order.createdtime;
	orderdata.message = order.content.message
	orderdata.items = [];
	_.each(order.content.goods, (orderGood) => {
		orderdata.items.push({
			title: orderGood.name,
			description: orderGood.specifications.join(),
			comment: orderGood.comment,
			number: orderGood.number,
			price: orderGood.price
		})
	});

	console.log(orderdata)

	axios.post('http://127.0.0.1:9031/printer', orderdata).then(response => {
		console.log(response);
	}).catch(err => {
		console.log(err)
	})

}
