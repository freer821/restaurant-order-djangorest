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

export function getForecast(id) {
  return request({
    url: '/forecasts/' + id,
    method: 'get'
  })
}

export function editForecast(data) {
  console.log(data)
  const id = data.id
  return request({
    url: '/forecasts/' + id + '/',
    method: 'put',
    data
  })
}

export function listAdminForecasts(params) {
  return request({
    url: '/admin/forecasts/',
    method: 'get',
    params
  })
}

export function rukuForecast(data, current_user) {
  return request({
    url: '/admin/forecasts/ruku_handle/?current_user=' + current_user,
    method: 'post',
    data
  })
}

