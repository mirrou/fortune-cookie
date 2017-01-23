#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomfortune():
    #make list of possible fortunes
    fortunes = [
    "If you can't beat them, arrange to have them beaten. <br> <em>-George Carlin</em>",
    "Always do whatever's next. <br> <em>-George Carlin</em>",
    "Don't sweat the petty things and don't pet the sweaty things. <br> <em>-George Carlin</em>",
    "There's no present.  There's only the immediate future and the recent past. <br> <em>-George Carlin</em>"
    ]
    #randomly select one of the fortunes
    index = random.randint(1,3)
    return fortunes[index]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomfortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence ='Your lucky number: ' + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_again_button = "<a href='.'><button>Another cookie, PLEASE!</button></a>"



        content = header + fortune_paragraph + number_paragraph + cookie_again_button

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
],debug=True)
