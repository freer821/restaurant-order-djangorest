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
    url: '/admin/product/',
    method: 'post',
    data
  })
}

export function getAdminDetailCheckedWares(params) {
  return request({
    url: '/admin/product/',
    method: 'get',
    params
  })
}

export function getDetailCheckedWare(id) {
  return request({
    url: '/admin/product/' + id,
    method: 'get'
  })
}

export function editDetailCheckedWare(data) {
  return request({
    url: '/admin/product/' + data.id + '/',
    method: 'put',
    data
  })
}

export function getUserWarehouseList(params) {
  return request({
    url: '/warehouse/',
    method: 'get',
    params
  })
}

export function getUserDetailCheckedWares(params) {
  return request({
    url: '/product/',
    method: 'get',
    params
  })
}
