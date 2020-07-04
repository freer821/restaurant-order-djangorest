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

export function pushMassivCheckedWares(data) {
  return request({
    url: '/admin/warehouse/massiv_check_handle/?current_user=2',
    method: 'post',
    data
  })
}

export function pushDetailCheckedWares(data) {
  return request({
    url: '/admin/warehousedetail/',
    method: 'post',
    data
  })
}
