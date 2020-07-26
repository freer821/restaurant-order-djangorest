import request from '@/utils/request'
export function listCategory(params) {
  return request({
    url: '/api/category/',
    method: 'get',
    params
  })
}

export function listGoods(params) {
  return request({
    url: '/api/good/',
    method: 'get',
    params
  })
}

export function getGood(id) {
  return request({
    url: '/api/good/' + id,
    method: 'get'
  })
}
