import request from '@/utils/request'

export function addForecast(data) {
  return request({
    url: '/forecasts/',
    method: 'post',
    data
  })
}

export function listForecasts(params) {
  return request({
    url: '/forecasts/',
    method: 'get',
    params
  })
}
