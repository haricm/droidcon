def gentable(data):
    colsizes = [3, 3, 3, 3]
    print '<ul class="grid schedule container-fluid">'
    headers = data[:2]
    for row in headers:
        print '  <li class="row-fluid header">'
        for counter, col in enumerate(row):
            print (u'    <div class="span%d">%s</div>' % (colsizes[counter], col or '&nbsp;')).encode('utf-8')
        print '  </li>'
    for row in data[2:]:
        print '  <li class="row-fluid item">'
        for counter, item in enumerate(row):
            if isinstance(item, dict):
                item['sectionname'] = '-'.join(item.get('section', '').lower().replace('&', '').replace(',', '').split(' '))
                item['levelname'] = '-'.join(item.get('level', '').lower().replace('&', '').replace(',', '').split(' '))
                print '    <div class="span%d">' % colsizes[counter]
                print '    <div class="session-box {sectionname}" title="{section}">'.format(**item)
                if item.get('url'):
                    print '      <a href="{url}" target="_blank">{title}</a><br><div class="author">{speaker}</div><br><div class="{levelname}" title="{level}"></div>'.format(**item)
                else:
                    print '      {title}<br>&mdash;{speaker}'.format(**item)
                print '    </div></div>'
            else:
                print (u'    <div class="span%d">%s</div>' % (colsizes[counter], item)).encode('utf-8')
        print '  </li>'
    print '</ul>'

sched1 = [['', 'Day 1', '', ''], ['Rooms', 'Audi', 'Hall', 'Room'], ['8:30-10:00', 'Registration & Introductions', '', ''], ['10:00-10:30', 'About Droidcon 2012', '', ''], ['10:30-11:00', {u'confirmed': True, u'name': u'506-the-real-incident-of-stealing-a-droid-app-data-in-daytime', u'title': u'The Real Incident of Stealing a Droid App+Data in daytime', u'url': u'http://funnel.hasgeek.com/droidcon2012/506-the-real-incident-of-stealing-a-droid-app-data-in-daytime', u'section': u'General Topics', u'level': u'Beginner', u'votes': 20, u'submitted': u'2012-09-03T03:24:31', u'email': None, u'proposer': u'Akash Mahajan', u'phone': None, u'speaker': u'Akash Mahajan', u'comments': 0, u'type': u'Lecture', u'id': 506}, {u'confirmed': True, u'name': u'504-mobile-user-experience-design-what-developers-usually-miss', u'title': u'Mobile User Experience Design - What developers usually miss', u'url': u'http://funnel.hasgeek.com/droidcon2012/504-mobile-user-experience-design-what-developers-usually-miss', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 18, u'submitted': u'2012-09-02T15:34:31', u'email': None, u'proposer': u'Amrit Sanjeev', u'phone': None, u'speaker': u'Amrit Sanjeev', u'comments': 0, u'type': u'Lecture', u'id': 504}, ''], ['11:00-11:30', {u'confirmed': True, u'name': u'523-augmented-reality-for-navigation-thru-the-galli', u'title': u'Augmented Reality for Navigation - Thru the Galli', u'url': u'http://funnel.hasgeek.com/droidcon2012/523-augmented-reality-for-navigation-thru-the-galli', u'section': u'App Demos', u'level': u'Beginner', u'votes': 21, u'submitted': u'2012-09-12T10:56:47', u'email': None, u'proposer': u'Anenth Guru', u'phone': None, u'speaker': u'Anenth Guru', u'comments': 3, u'type': u'Demo', u'id': 523}, {u'confirmed': True, u'name': u'549-android-ui-prototyping-101-what-why-how', u'title': u'Android UI prototyping 101: What? Why? How?', u'url': u'http://funnel.hasgeek.com/droidcon2012/549-android-ui-prototyping-101-what-why-how', u'section': u'General Topics', u'level': u'Beginner', u'votes': 15, u'submitted': u'2012-10-04T10:16:04', u'email': None, u'proposer': u'Soham Mondal', u'phone': None, u'speaker': u'Soham Mondal', u'comments': 6, u'type': u'Lecture', u'id': 549}, ''], ['11:30-12:00', 'Break', 'Break', ''], ['12:00-12:30', {u'confirmed': True, u'name': u'547-move-as-i-speak', u'title': u'Move as i speak', u'url': u'http://funnel.hasgeek.com/droidcon2012/547-move-as-i-speak', u'section': u'Specialized Topics', u'level': u'Beginner', u'votes': 32, u'submitted': u'2012-10-01T18:07:19', u'email': None, u'proposer': u'Phanindra Rachamalla', u'phone': None, u'speaker': u'Phanindra Rachamalla', u'comments': 2, u'type': u'Demo', u'id': 547}, {u'confirmed': True, u'name': u'553-the-state-of-web-and-native-in-2012', u'title': u'The State of Web AND Native in 2012', u'url': u'http://funnel.hasgeek.com/droidcon2012/553-the-state-of-web-and-native-in-2012', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 5, u'submitted': u'2012-10-08T21:54:33', u'email': None, u'proposer': u'James Hugman', u'phone': None, u'speaker': u'James Hugman', u'comments': 0, u'type': u'Lecture', u'id': 553}, ''], ['12:30-1:00', {u'confirmed': True, u'name': u'517-location-based-shopping-application-delightcircle', u'title': u'Location Based Shopping Application - DelightCircle ', u'url': u'http://funnel.hasgeek.com/droidcon2012/517-location-based-shopping-application-delightcircle', u'section': u'App Demos', u'level': u'Intermediate', u'votes': 24, u'submitted': u'2012-09-10T19:37:23', u'email': None, u'proposer': u'Yashwanth Kumar', u'phone': None, u'speaker': u'Yashwanth Kumar', u'comments': 2, u'type': u'Demo', u'id': 517}, {u'confirmed': True, u'name': u'553-the-state-of-web-and-native-in-2012', u'title': u'The State of Web AND Native in 2012', u'url': u'http://funnel.hasgeek.com/droidcon2012/553-the-state-of-web-and-native-in-2012', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 5, u'submitted': u'2012-10-08T21:54:33', u'email': None, u'proposer': u'James Hugman', u'phone': None, u'speaker': u'James Hugman', u'comments': 0, u'type': u'Lecture', u'id': 553}, ''], ['1:00-2:00', 'Lunch', 'Lunch', 'Lunch'], ['2:00-2:30', {u'confirmed': True, u'name': u'497-microsoft-kinect-and-android', u'title': u'Microsoft Kinect and Android', u'url': u'http://funnel.hasgeek.com/droidcon2012/497-microsoft-kinect-and-android', u'section': u'App Demos', u'level': u'Intermediate', u'votes': 21, u'submitted': u'2012-08-31T14:42:56', u'email': None, u'proposer': u'Allen Thomas Varghese', u'phone': None, u'speaker': u'Allen Thomas Varghese', u'comments': 4, u'type': u'Demo', u'id': 497}, {u'confirmed': True, u'name': u'583-lets-code-an-android-app-with-javascript-using-titanium', u'title': u'Lets Code an Android App with "Javascript" using Titanium', u'url': u'http://funnel.hasgeek.com/droidcon2012/583-lets-code-an-android-app-with-javascript-using-titanium', u'section': u'App Demos', u'level': u'Beginner', u'votes': 31, u'submitted': u'2012-10-21T07:12:36', u'email': None, u'proposer': u'Ravindra Kumar', u'phone': None, u'speaker': u'Ravindra Kumar', u'comments': 1, u'type': u'Demo', u'id': 583}, {u'confirmed': True, u'name': u'483-behind-the-scenes-creating-android-devices', u'title': u'Behind the Scenes : Creating Android Devices', u'url': u'http://funnel.hasgeek.com/droidcon2012/483-behind-the-scenes-creating-android-devices', u'section': u'Platforms, Tools & Libraries', u'level': u'Beginner', u'votes': 17, u'submitted': u'2012-08-30T07:16:27', u'email': None, u'proposer': u'Shree Kumar', u'phone': None, u'speaker': u'Shree Kumar', u'comments': 0, u'type': u'Lecture', u'id': 483}], ['2:30-3:00', {u'confirmed': True, u'name': u'444-nosql-location-based-queries-on-android-couchdb-mobile-replication-and-lucene', u'title': u'NoSQL & Location based queries on Android - CouchDB, Mobile Replication and Lucene', u'url': u'http://funnel.hasgeek.com/droidcon2012/444-nosql-location-based-queries-on-android-couchdb-mobile-replication-and-lucene', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 23, u'submitted': u'2012-08-08T04:58:01', u'email': None, u'proposer': u'Sameer Segal', u'phone': None, u'speaker': u'Sameer Segal', u'comments': 3, u'type': u'Tutorial', u'id': 444}, {u'confirmed': True, u'name': u'548-using-appcelerator-titanium-to-build-native-android-apps-without-the-native-pain', u'title': u'Using Appcelerator Titanium To Build Native Android Apps Without The Native Pain', u'url': u'http://funnel.hasgeek.com/droidcon2012/548-using-appcelerator-titanium-to-build-native-android-apps-without-the-native-pain', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 11, u'submitted': u'2012-10-03T11:15:12', u'email': None, u'proposer': u'Gaurav Kheterpal', u'phone': None, u'speaker': u'Gaurav Kheterpal', u'comments': 0, u'type': u'Workshop', u'id': 548}, {u'confirmed': True, u'name': u'595-building-your-app-for-multiple-app-stores', u'title': u'Building your app for multiple app stores ', u'url': u'http://funnel.hasgeek.com/droidcon2012/595-building-your-app-for-multiple-app-stores', u'section': u'Workshops', u'level': u'Beginner', u'votes': 5, u'submitted': u'2012-10-30T00:28:31', u'email': None, u'proposer': u'Timur Dyussebayev', u'phone': None, u'speaker': u'Timur Dyussebayev', u'comments': 0, u'type': u'Workshop', u'id': 595}], ['3:00-3:30', {u'confirmed': True, u'name': u'499-constructive-design-for-android', u'title': u'Constructive Design for Android', u'url': u'http://funnel.hasgeek.com/droidcon2012/499-constructive-design-for-android', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 27, u'submitted': u'2012-08-31T14:58:10', u'email': None, u'proposer': u'Isaac Wesley', u'phone': None, u'speaker': u'Isaac Wesley', u'comments': 0, u'type': u'Lecture', u'id': 499}, {u'confirmed': True, u'name': u'586-cross-platform-development-bridging-the-gap', u'title': u'Cross Platform Development: Bridging the Gap', u'url': u'http://funnel.hasgeek.com/droidcon2012/586-cross-platform-development-bridging-the-gap', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 7, u'submitted': u'2012-10-22T05:54:15', u'email': None, u'proposer': u'Priyank Gupta', u'phone': None, u'speaker': u'Priyank Gupta', u'comments': 0, u'type': u'Lecture', u'id': 586}, {u'confirmed': True, u'name': u'595-building-your-app-for-multiple-app-stores', u'title': u'Building your app for multiple app stores ', u'url': u'http://funnel.hasgeek.com/droidcon2012/595-building-your-app-for-multiple-app-stores', u'section': u'Workshops', u'level': u'Beginner', u'votes': 5, u'submitted': u'2012-10-30T00:28:31', u'email': None, u'proposer': u'Timur Dyussebayev', u'phone': None, u'speaker': u'Timur Dyussebayev', u'comments': 0, u'type': u'Workshop', u'id': 595}], ['3:30-4:00', 'Break', 'Break', 'Break'], ['4:00-4:30', {u'confirmed': True, u'name': u'587-using-websockets-to-control-robots-in-realtime', u'title': u'Using websockets to control robots in realtime', u'url': u'http://funnel.hasgeek.com/droidcon2012/587-using-websockets-to-control-robots-in-realtime', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 6, u'submitted': u'2012-10-23T16:34:31', u'email': None, u'proposer': u'Sudar Muthu', u'phone': None, u'speaker': u'Sudar Muthu', u'comments': 0, u'type': u'Lecture', u'id': 587}, {u'confirmed': True, u'name': u'537-why-what-how-of-monetization-using-ads', u'title': u'Why, What & How of Monetization using Ads', u'url': u'http://funnel.hasgeek.com/droidcon2012/537-why-what-how-of-monetization-using-ads', u'section': u'General Topics', u'level': u'Beginner', u'votes': 22, u'submitted': u'2012-09-24T18:04:14', u'email': None, u'proposer': u'Ravi Vyas', u'phone': None, u'speaker': u'Ravi Vyas', u'comments': 3, u'type': u'Lecture', u'id': 537}, {u'confirmed': True, u'name': u'592-what-we-learnt-during-the-making-of-cosmos', u'title': u'What we learnt during the making of Cosmos', u'url': u'http://funnel.hasgeek.com/droidcon2012/592-what-we-learnt-during-the-making-of-cosmos', u'section': u'App Demos', u'level': u'Intermediate', u'votes': 3, u'submitted': u'2012-10-29T08:53:51', u'email': None, u'proposer': u'SDC Bangalore', u'phone': None, u'speaker': u'SDC Bangalore', u'comments': 0, u'type': u'Demo', u'id': 592}], ['4:30-5:00', {u'confirmed': True, u'name': u'587-using-websockets-to-control-robots-in-realtime', u'title': u'Using websockets to control robots in realtime', u'url': u'http://funnel.hasgeek.com/droidcon2012/587-using-websockets-to-control-robots-in-realtime', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 6, u'submitted': u'2012-10-23T16:34:31', u'email': None, u'proposer': u'Sudar Muthu', u'phone': None, u'speaker': u'Sudar Muthu', u'comments': 0, u'type': u'Lecture', u'id': 587}, '', ''], ['5:00-6:00', 'Open Time - Social', '', ''], ['6:00-10:00', 'Event Dinner Party @ Counter Culture\n(featuring live performance by Ministry of Blues)', '', '']]
sched2 = [['', 'Day 2', '', ''], ['Rooms', 'Audi', 'Hall', 'Room'], ['9:00-10:00', 'Registration', '', ''], ['10:00-10:30', {u'confirmed': True, u'name': u'556-writing-toolkits-frameworks-and-plugins-a-developer-masterclass-in-writing-re-usable-code', u'title': u'Writing Toolkits, Frameworks and Plugins. A Developer Masterclass in Writing Re-usable Code.', u'url': u'http://funnel.hasgeek.com/droidcon2012/556-writing-toolkits-frameworks-and-plugins-a-developer-masterclass-in-writing-re-usable-code', u'section': u'General Topics', u'level': u'Advanced', u'votes': 1, u'submitted': u'2012-10-08T23:33:17', u'email': None, u'proposer': u'James Hugman', u'phone': None, u'speaker': u'James Hugman', u'comments': 0, u'type': u'Lecture', u'id': 556}, {u'confirmed': True, u'name': u'588-android-application-development-a-crash-course', u'title': u'Android application development: a crash course', u'url': u'http://funnel.hasgeek.com/droidcon2012/588-android-application-development-a-crash-course', u'section': u'Workshops', u'level': u'Beginner', u'votes': 5, u'submitted': u'2012-10-24T18:34:47', u'email': None, u'proposer': u'Soham Mondal', u'phone': None, u'speaker': u'Soham Mondal', u'comments': 2, u'type': u'Workshop', u'id': 588}, ''], ['10:30-11:00', {u'confirmed': True, u'name': u'556-writing-toolkits-frameworks-and-plugins-a-developer-masterclass-in-writing-re-usable-code', u'title': u'Writing Toolkits, Frameworks and Plugins. A Developer Masterclass in Writing Re-usable Code.', u'url': u'http://funnel.hasgeek.com/droidcon2012/556-writing-toolkits-frameworks-and-plugins-a-developer-masterclass-in-writing-re-usable-code', u'section': u'General Topics', u'level': u'Advanced', u'votes': 1, u'submitted': u'2012-10-08T23:33:17', u'email': None, u'proposer': u'James Hugman', u'phone': None, u'speaker': u'James Hugman', u'comments': 0, u'type': u'Lecture', u'id': 556}, {u'confirmed': True, u'name': u'588-android-application-development-a-crash-course', u'title': u'Android application development: a crash course', u'url': u'http://funnel.hasgeek.com/droidcon2012/588-android-application-development-a-crash-course', u'section': u'Workshops', u'level': u'Beginner', u'votes': 5, u'submitted': u'2012-10-24T18:34:47', u'email': None, u'proposer': u'Soham Mondal', u'phone': None, u'speaker': u'Soham Mondal', u'comments': 2, u'type': u'Workshop', u'id': 588}, ''], ['11:00-11:30', {u'confirmed': True, u'name': u'580-dr-droidlove-a-k-a-how-i-learned-to-stop-worrying-and-love-the-fragmentation', u'title': u'Dr DroidLove a.k.a How I Learned to Stop Worrying and Love the Fragmentation', u'url': u'http://funnel.hasgeek.com/droidcon2012/580-dr-droidlove-a-k-a-how-i-learned-to-stop-worrying-and-love-the-fragmentation', u'section': u'General Topics', u'level': u'Intermediate', u'votes': 21, u'submitted': u'2012-10-19T06:11:25', u'email': None, u'proposer': u'Aditya Shankar', u'phone': None, u'speaker': u'Aditya Shankar', u'comments': 0, u'type': u'Lecture', u'id': 580}, {u'confirmed': True, u'name': u'577-take-your-android-app-offline-with-sms', u'title': u'Take your Android app offline with SMS ', u'url': u'http://funnel.hasgeek.com/droidcon2012/577-take-your-android-app-offline-with-sms', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 28, u'submitted': u'2012-10-17T18:27:43', u'email': None, u'proposer': u'Gopi Krishnan', u'phone': None, u'speaker': u'Gopi Krishnan', u'comments': 1, u'type': u'Lecture', u'id': 577}, ''], ['11:30-12:00', 'Break', 'Break', ''], ['12:00-12:30', {u'confirmed': True, u'name': u'574-using-mat-memory-analyzer-tool-to-understand-memory-issues-in-your-app', u'title': u'Using MAT (Memory Analyzer Tool) to understand memory issues in your app', u'url': u'http://funnel.hasgeek.com/droidcon2012/574-using-mat-memory-analyzer-tool-to-understand-memory-issues-in-your-app', u'section': u'Platforms, Tools & Libraries', u'level': u'Beginner', u'votes': 7, u'submitted': u'2012-10-16T18:19:15', u'email': None, u'proposer': u'Kakkirala Lakshman', u'phone': None, u'speaker': u'Kakkirala Lakshman', u'comments': 0, u'type': u'Tutorial', u'id': 574}, {u'confirmed': True, u'name': u'571-agile-development-for-mobile-apps', u'title': u'Agile development for mobile apps', u'url': u'http://funnel.hasgeek.com/droidcon2012/571-agile-development-for-mobile-apps', u'section': u'General Topics', u'level': u'Intermediate', u'votes': 16, u'submitted': u'2012-10-16T11:57:02', u'email': None, u'proposer': u'Rajaram', u'phone': None, u'speaker': u'Rajaram', u'comments': 0, u'type': u'Lecture', u'id': 571}, ''], ['12:30-1:00', {u'confirmed': True, u'name': u'527-optimizing-for-battery-measuring-and-managing-power-consumption-of-android-apps', u'title': u'Optimizing for Battery - Measuring and managing power consumption of Android apps', u'url': u'http://funnel.hasgeek.com/droidcon2012/527-optimizing-for-battery-measuring-and-managing-power-consumption-of-android-apps', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 11, u'submitted': u'2012-09-14T11:38:28', u'email': None, u'proposer': u'Kumar Rangarajan', u'phone': None, u'speaker': u'Kumar Rangarajan', u'comments': 0, u'type': u'Demo', u'id': 527}, {u'confirmed': True, u'name': u'570-hacking-android-for-fun-and-profit', u'title': u'Hacking Android for Fun and Profit', u'url': u'http://funnel.hasgeek.com/droidcon2012/570-hacking-android-for-fun-and-profit', u'section': u'Specialized Topics', u'level': u'Advanced', u'votes': 8, u'submitted': u'2012-10-16T11:42:10', u'email': None, u'proposer': u'Indraneel Bommisetty', u'phone': None, u'speaker': u'Indraneel Bommisetty', u'comments': 0, u'type': u'Lecture', u'id': 570}, ''], ['1:00-2:00', 'Lunch', '', ''], ['2:00-2:30', 'Hacknight Demos', {u'confirmed': True, u'name': u'475-indian-language-app-development-framework-for-android-2-x', u'title': u'Indian Language App.Development Framework for Android 2.x', u'url': u'http://funnel.hasgeek.com/droidcon2012/475-indian-language-app-development-framework-for-android-2-x', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 15, u'submitted': u'2012-08-26T12:52:17', u'email': None, u'proposer': u'SijiSunny', u'phone': None, u'speaker': u'SijiSunny', u'comments': 2, u'type': u'Lecture', u'id': 475}, {u'confirmed': True, u'name': u'545-android-accessory-development-with-beaglebone', u'title': u'Android Accessory development with Beaglebone', u'url': u'http://funnel.hasgeek.com/droidcon2012/545-android-accessory-development-with-beaglebone', u'section': u'Specialized Topics', u'level': u'Beginner', u'votes': 15, u'submitted': u'2012-09-26T13:27:21', u'email': None, u'proposer': u'Pankaj Bharadiya', u'phone': None, u'speaker': u'Pankaj Bharadiya', u'comments': 0, u'type': u'Lecture', u'id': 545}], ['2:30-3:00', 'App Jam - 5 minute elevator pitches', {u'confirmed': True, u'name': u'590-exploring-the-ketai-library-for-faster-development-of-advanced-android-features', u'title': u"Exploring the 'ketai' library for faster development of advanced android features", u'url': u'http://funnel.hasgeek.com/droidcon2012/590-exploring-the-ketai-library-for-faster-development-of-advanced-android-features', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 20, u'submitted': u'2012-10-26T02:49:54', u'email': None, u'proposer': u'Sriram Narasimhan', u'phone': None, u'speaker': u'Sriram Narasimhan', u'comments': 3, u'type': u'Demo', u'id': 590}, {u'confirmed': True, u'name': u'593-introduction-to-android-x86-platform', u'title': u'Introduction to Android x86 Platform', u'url': u'http://funnel.hasgeek.com/droidcon2012/593-introduction-to-android-x86-platform', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 2, u'submitted': u'2012-10-29T11:14:18', u'email': None, u'proposer': u'Premchander Rao T', u'phone': None, u'speaker': u'Premchander Rao T', u'comments': 0, u'type': u'Lecture', u'id': 593}], ['3:00-3:30', {u'confirmed': True, u'name': u'576-advanced-controls-for-android-games', u'title': u'Advanced Controls for Android Games', u'url': u'http://funnel.hasgeek.com/droidcon2012/576-advanced-controls-for-android-games', u'section': u'Specialized Topics', u'level': u'Intermediate', u'votes': 37, u'submitted': u'2012-10-17T09:46:00', u'email': None, u'proposer': u'umashankar chidige', u'phone': None, u'speaker': u'umashankar chidige', u'comments': 6, u'type': u'Lecture', u'id': 576}, {u'confirmed': True, u'name': u'561-mymobiledash-a-drupal-based-platform-for-mobile-apps', u'title': u'Mymobiledash - A Drupal based Platform for Mobile apps', u'url': u'http://funnel.hasgeek.com/droidcon2012/561-mymobiledash-a-drupal-based-platform-for-mobile-apps', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 23, u'submitted': u'2012-10-11T15:03:42', u'email': None, u'proposer': u'Prateek Jain', u'phone': None, u'speaker': u'Prateek Jain', u'comments': 5, u'type': u'Lecture', u'id': 561}, {u'confirmed': True, u'name': u'593-introduction-to-android-x86-platform', u'title': u'Introduction to Android x86 Platform', u'url': u'http://funnel.hasgeek.com/droidcon2012/593-introduction-to-android-x86-platform', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 2, u'submitted': u'2012-10-29T11:14:18', u'email': None, u'proposer': u'Premchander Rao T', u'phone': None, u'speaker': u'Premchander Rao T', u'comments': 0, u'type': u'Lecture', u'id': 593}], ['3:30-4:00', 'Break', '', ''], ['4:00-4:30', {u'confirmed': True, u'name': u'584-building-the-flipkart-flyte-mp3-app-the-lean-startup-way', u'title': u"Building the Flipkart Flyte MP3 app, the 'Lean Startup' way", u'url': u'http://funnel.hasgeek.com/droidcon2012/584-building-the-flipkart-flyte-mp3-app-the-lean-startup-way', u'section': u'Specialized Topics', u'level': u'Beginner', u'votes': 9, u'submitted': u'2012-10-21T13:51:58', u'email': None, u'proposer': u'Gaurav Lochan', u'phone': None, u'speaker': u'Gaurav Lochan', u'comments': 0, u'type': u'Lecture', u'id': 584}, {u'confirmed': True, u'name': u'471-deep-dive-into-gcm-google-cloud-messaging-for-android', u'title': u'Deep Dive into GCM ( Google Cloud Messaging) for Android', u'url': u'http://funnel.hasgeek.com/droidcon2012/471-deep-dive-into-gcm-google-cloud-messaging-for-android', u'section': u'Specialized Topics', u'level': u'Beginner', u'votes': 10, u'submitted': u'2012-08-24T10:19:20', u'email': None, u'proposer': u'prajyot mainkar', u'phone': None, u'speaker': u'prajyot mainkar', u'comments': 1, u'type': u'Tutorial', u'id': 471}, {u'confirmed': True, u'name': u'536-opencv-image-processing-applications-with-android', u'title': u'OpenCV Image processing applications with Android', u'url': u'http://funnel.hasgeek.com/droidcon2012/536-opencv-image-processing-applications-with-android', u'section': u'Platforms, Tools & Libraries', u'level': u'Intermediate', u'votes': 9, u'submitted': u'2012-09-24T06:17:36', u'email': None, u'proposer': u'Wingston Sharon', u'phone': None, u'speaker': u'Wingston Sharon', u'comments': 0, u'type': u'Workshop', u'id': 536}], ['4:30-5:00', {u'confirmed': True, u'name': u'591-joke-joke', u'title': u'Joke, joke', u'url': u'http://funnel.hasgeek.com/droidcon2012/591-joke-joke', u'section': u'Specialized Topics', u'level': u'Advanced', u'votes': 6, u'submitted': u'2012-10-28T11:07:03', u'email': None, u'proposer': u'Koushik', u'phone': None, u'speaker': u'Koushik', u'comments': 0, u'type': u'Lecture', u'id': 591}, '', ''], ['5:00-5:30', 'Thanks & Feedback', '', ''], ['5:30-6:00', 'Planning Droidcon 2013', '', '']]

gentable(sched1)
gentable(sched2)
