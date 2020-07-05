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
    url: '/chuku/',
    method: 'get',
    params
  })
}

export function getUserChuku(id) {
  return request({
    url: '/chuku/' + id,
    method: 'get'
  })
}

export function updateUserChuku(data) {
  return request({
    url: '/chuku/' + data.id + '/',
    method: 'put',
    data
  })
}

export function listAdminChuku(params) {
  return request({
    url: '/admin/chuku/',
    method: 'get',
    params
  })
}

export function getAdminChuku(id) {
  return request({
    url: '/admin/chuku/' + id,
    method: 'get'
  })
}

export function updateAdminChuku(data) {
  console.log(data)
  return request({
    url: '/admin/chuku/' + data.id + '/',
    method: 'put',
    data
  })
}

