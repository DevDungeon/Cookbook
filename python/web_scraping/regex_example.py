import re

haystack = 'asdfasdfasdf<script src="aasdf">javascr\nipt\nh\ne\nre</script>asdfasdfasdfasdf'

needle = '<script(.|\n)*</script>'
# needle = '<img(.|\n)*>'
# needle = '<a.*</a>'

re_match = re.search(needle, haystack)
matching_text = re_match.group(0)
print(matching_text)
