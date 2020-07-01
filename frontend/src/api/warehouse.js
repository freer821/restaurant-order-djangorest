import request from '@/utils/request'

export function getAdminWarehouseList(params) {
  return request({
    url: '/admin/warehouse/',
    method: 'get',
    params
  })
}

export function updateAdminWarehouseList(data) {
  return request({
    url: '/admin/warehouse/' + data.id + '/',
    method: 'put',
    data
  })
}
