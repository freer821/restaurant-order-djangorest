import request from '@/utils/request'

export function listStorage(query) {
  return request({
    url: '/api/store',
    method: 'get',
    params: query
  })
}

export function createStorage(data) {
  return request({
    url: '/api/store/',
    method: 'post',
    data
  })
}

export function delStorage(id) {
  return request({
    url: '/api/store/' + id + '/',
    method: 'DELETE'
  })
}

export function listAdminStorage(query) {
  return request({
    url: '/api/admin/store',
    method: 'get',
    params: query
  })
}

export function createAdminStorage(data) {
  return request({
    url: '/api/admin/store/',
    method: 'post',
    data
  })
}

export function delAdminStorage(id) {
  return request({
    url: '/api/admin/store/' + id + '/',
    method: 'DELETE'
  })
}
