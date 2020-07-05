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
    url: '/chuku/',
    method: 'put',
    data
  })
}
