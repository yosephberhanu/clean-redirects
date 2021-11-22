# Track redirects with in a file
### Brief
A script to parse all links with in a file and replace them with the final destination URL if they had redirects
### Background
URL redirection, also known as URL forwarding, is a technique to give more than one URL address to a page, a form, or a whole Web site/application. HTTP has a special kind of response, called a HTTP redirect, for this operation.

Redirects accomplish numerous goals:
* Temporary redirects during site maintenance or downtime
* Permanent redirects to preserve existing links/bookmarks after changing the site's URLs, progress pages when uploading a file, etc.
* Websites that host a link to an external content could redirect the links through their server to perform an analytics every time a user clicks on a link

### Objective
This script cleans a text file in order to replace links with in the file that are meant to go through a serious of redirects with the final URL

### How to run
python clean-redirectspy -f < input_file >

