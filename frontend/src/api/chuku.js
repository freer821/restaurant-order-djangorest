import request from '@/utils/request'

export function createUserChuku(data) {
  return request({
    url: '/chuku/',
    method: 'post',
    data
  })
}

export function listUserChuku(params) {
  return request({
    url: '/api/chuku/',
    method: 'get',
    params
  })
}

export function getUserChuku(id) {
  return request({
    url: '/api/chuku/' + id,
    method: 'get'
  })
}

export function updateUserChuku(data) {
  return request({
    url: '/api/chuku/' + data.id + '/',
    method: 'put',
    data
  })
}

export function listAdminChuku(params) {
  return request({
    url: '/api/admin/chuku/',
    method: 'get',
    params
  })
}

export function createAdminChuku(data) {
  return request({
    url: '/api/admin/chuku/',
    method: 'post',
    data
  })
}

export function getAdminChuku(id) {
  return request({
    url: '/api/admin/chuku/' + id,
    method: 'get'
  })
}

export function updateAdminChuku(data) {
  console.log(data)
  return request({
    url: '/api/admin/chuku/' + data.id + '/',
    method: 'put',
    data
  })
}

export function delAdminChuku(id) {
  return request({
    url: '/api/admin/chuku/' + id + '/',
    method: 'DELETE'
  })
}

