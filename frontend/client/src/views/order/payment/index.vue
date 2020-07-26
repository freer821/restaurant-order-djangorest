<template>
	<div class="payment">
		<div class="time_down payment_group">
			Only Credit Card accepted! Please finish the Payment
			<span class="red">in 30 minutes</span>
			，Otherwise this Order will be canceled!
		</div>

		<van-cell-group class="payment_group">
			<van-cell title="Total:">
				<span class="red">{{order.fee *100 | euro}}</span>
			</van-cell>
			<van-field
				v-model="order.content.message"
				placeholder="Comment"
				label="Comment"
			>
				<template slot="icon">{{order.content.message.length}}/50</template>
			</van-field>
		</van-cell-group>

		<div class="pay_way_group">
			<div class="pay_way_title">Eat Way</div>
			<van-radio-group v-model="order.type">
				<van-cell-group>
					<van-cell title="Eat in">
						<van-radio name="eatin"/>
					</van-cell>
					<van-cell title="Take Away">
						<van-radio name="takeaway"/>
					</van-cell>
				</van-cell-group>
			</van-radio-group>
		</div>


		<div class="pay_cancel_div">
			<van-button
				class="pay_submit"
				@click="pay"
				type="primary"
				bottomAction
			>Pay
			</van-button>
			<van-button
				class="cancel_submit"
				@click="cancel"
				type="danger"
				bottomAction
			>Canel
			</van-button>
		</div>
	</div>
</template>

<script>
	import {Radio, RadioGroup, Dialog, Field} from 'vant';
	import {createOrder} from '@/api/api';
	import {printOrder} from '@/utils/cart'
	export default {
		name: 'payment',

		data() {
			return {
				order: {
					type: 'eatin',
					fee: this.$store.getters.fee_cart_goods,
					content: {
						message: '',
						goods: Object.values(this.$store.getters.cart_goods),
					},
					status: 'created'
				}
			};
		},
		methods: {
			pay() {
				createOrder(this.order).then(response => {
					this.$store.dispatch('order/setOrder', response.data)
					Dialog.confirm({
						message: 'Please insert your Credit Cart and input your PIN!'
					})
						.then(() => {
							this.$store.dispatch('cart/clearCart')
							this.$router.push('/');
							printOrder(this.$store.getters.order)
						})
						.catch(err => {
							console.log(err);
						});

				}).catch(err => {
					console.log(err)
				})
			},
			cancel() {
				Dialog.confirm({
					title: 'Order Cancel!',
					message: 'after canceling this order, all of the Cart will be removed'
				}).then(() => {
					this.$router.push('/');
				});
			}
		},

		components: {
			[Radio.name]: Radio,
			[RadioGroup.name]: RadioGroup,
			[Dialog.name]: Dialog,
			[Field.name]: Field
		}
	};
</script>

<style lang="scss" scoped>
	.payment_group {
		margin-bottom: 10px;
	}

	.time_down {
		background-color: #fffeec;
		padding: 10px 15px;
	}

	.pay_submit {
		width: 100%;
	}

	.cancel_submit {
		width: 100%;
	}

	.pay_cancel_div {
		position: fixed;
		bottom: 0;
		width: 100%;
	}


	.pay_way_group img {
		vertical-align: middle;
	}

	.pay_way_title {
		padding: 15px;
		background-color: #fff;
	}
</style>
