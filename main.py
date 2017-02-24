# coding=utf-8

import webapp2
import httplib


class DefaultHandler(webapp2.RequestHandler):
    def get(self):
        app_url = self.request.application_url

        self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'

        self.response.write('KBS 클래식FM: %s/kbs1\n' % app_url)
        self.response.write('KBS 쿨FM: %s/kbs2\n' % app_url)
        self.response.write('KBS 1라디오: %s/kbs1r\n' % app_url)
        self.response.write('KBS 2라디오: %s/kbs2r\n' % app_url)
        self.response.write('KBS 3라디오: %s/kbs3r\n' % app_url)
        self.response.write('KBS 한민족방송: %s/kbsscr\n' % app_url)
        self.response.write('KBS 월드 라디오: %s/kbsrki\n' % app_url)


class KbsHandler(webapp2.RequestHandler):
    CHANNELS = {
        'kbs1': 1,
        'kbs2': 2,
        'kbs1r': 3,
        'kbs2r': 4,
        'kbs3r': 5,
        # Perhaps 6 is for DMB...
        'kbsscr': 7,
        'kbsrki': 8,
    }
    BASE_URL = \
        'http://kong.kbs.co.kr/live_player/channelMini.php' \
        + '?id=juoradio' \
        + '&channel=%d'

    def get(self, channel):
        try:
            channel_num = self.CHANNELS[channel]
            self.redirect(self.getAddress(channel_num))
        except KeyError:
            self.redirect('/')

    def getAddress(self, channel_num):
        conn = httplib.HTTPConnection('kbs_radio_stream', 80)
        conn.request('GET', self.BASE_URL % channel_num)
        responseString = conn.getresponse().read()
        conn.close()

        startIndex = responseString.find('mms:')
        return responseString[startIndex:]


app = webapp2.WSGIApplication(routes=[
    ('/', DefaultHandler),
    (r'/(.+)', KbsHandler),
    ])
