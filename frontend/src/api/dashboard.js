import request from '@/utils/request'

export function info(query) {
  return request({
    url: '/api/dashboard',
    method: 'get',
    params: query
  })
}
