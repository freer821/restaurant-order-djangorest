import request from '@/utils/request'

export function addForecast(data) {
  return request({
    url: '/api/forecasts/',
    method: 'post',
    data
  })
}

export function listForecasts(params) {
  return request({
    url: '/api/forecasts/',
    method: 'get',
    params
  })
}

export function getForecast(id) {
  return request({
    url: '/api/forecasts/' + id,
    method: 'get'
  })
}

export function editForecast(data) {
  return request({
    url: '/api/forecasts/' + data.id + '/',
    method: 'put',
    data
  })
}

export function delForecast(id) {
  return request({
    url: '/api/forecasts/' + id + '/',
    method: 'DELETE'
  })
}

export function listAdminForecasts(params) {
  return request({
    url: '/api/admin/forecasts/',
    method: 'get',
    params
  })
}

export function rukuForecast(data, current_user) {
  return request({
    url: '/api/admin/forecasts/ruku_handle/?current_user=' + current_user,
    method: 'post',
    data
  })
}

export function getForecastAdmin(id) {
  return request({
    url: '/api/admin/forecasts/' + id,
    method: 'get'
  })
}

export function updateForecastAdmin(data) {
  return request({
    url: '/api/admin/forecasts/' + data.id + '/',
    method: 'put',
    data
  })
}

export function createForecastAdmin(data) {
  return request({
    url: '/api/admin/forecasts/',
    method: 'post',
    data
  })
}

