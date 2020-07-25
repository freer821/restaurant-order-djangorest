import request from '@/utils/request'

export function listGoodsAdmin(params) {
  return request({
    url: '/api/admin/good/',
    method: 'get',
    params
  })
}

export function getGoodAdmin(id) {
  return request({
    url: '/api/admin/good/' + id,
    method: 'get'
  })
}

export function updateGoodAdmin(data) {
  return request({
    url: '/api/admin/good/' + data.id + '/',
    method: 'put',
    data
  })
}

export function createGoodAdmin(data) {
  return request({
    url: '/api/admin/good/',
    method: 'post',
    data
  })
}

export function delGoodAdmin(id) {
  return request({
    url: '/api/admin/good/' + id + '/',
    method: 'DELETE'
  })
}
