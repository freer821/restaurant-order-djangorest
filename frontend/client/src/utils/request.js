import axios from 'axios'
import {Dialog, Toast} from 'vant';
import store from '@/store'
import {getToken} from '@/utils/auth'


// create an axios instance
const service = axios.create({
	baseURL: process.env.VUE_APP_BASE_API, // api 的 base_url
	timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
	config => {
		if (!config.headers['X-Litemall-Token']) {
			if (store.getters.token) {
				config.headers['X-Litemall-Token'] = getToken();
			}
		}
		return config;
	},
	err => Promise.reject(err)
)

// response interceptor
service.interceptors.response.use(
	response => {
		const res = response.data

		if (res.status === 404) {
			Toast.fail('Not Found');
			return Promise.reject(res)
		} else if (res.status !== 200) {
			// 非200的错误属于业务错误，留给具体页面处理
			return Promise.reject(res)
		} else {
			return Promise.resolve(res)
		}
	}, error => {
		console.log('err' + error)// for debug
		Dialog.alert({
			title: 'Warning',
			message: 'conntect timeout'
		});
		return Promise.reject(error)
	})

export default service
