import request from '@/utils/request'

export function createUserChuku(data) {
  return request({
    url: '/ruku/',
    method: 'post',
    data
  })
}
