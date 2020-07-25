import request from '@/utils/request'

export function addCategory(data) {
  return request({
    url: '/api/category/',
    method: 'post',
    data
  })
}

export function listCategory(params) {
  return request({
    url: '/api/category/',
    method: 'get',
    params
  })
}

export function getCategory(id) {
  return request({
    url: '/api/category/' + id,
    method: 'get'
  })
}

export function editCategory(data) {
  return request({
    url: '/api/category/' + data.id + '/',
    method: 'put',
    data
  })
}

export function delCategory(id) {
  return request({
    url: '/api/category/' + id + '/',
    method: 'DELETE'
  })
}

export function listAdmincategory(params) {
  return request({
    url: '/api/admin/category/',
    method: 'get',
    params
  })
}

export function getCategoryAdmin(id) {
  return request({
    url: '/api/admin/category/' + id,
    method: 'get'
  })
}

export function updateCategoryAdmin(data) {
  return request({
    url: '/api/admin/category/' + data.id + '/',
    method: 'put',
    data
  })
}

export function createCategoryAdmin(data) {
  return request({
    url: '/api/admin/category/',
    method: 'post',
    data
  })
}

export function delCategoryAdmin(id) {
  return request({
    url: '/api/admin/category/' + id + '/',
    method: 'DELETE'
  })
}
