# https://github.com/schacon/ruby-git
# gem install git

require 'git'
require 'logger'

g = Git.open("../", :log => Logger.new(STDOUT))

puts g.index
puts g.index.readable?
puts g.index.writable?
puts g.repo
puts g.dir

g.log   # returns array of Git::Commit objects
g.log.since('2 weeks ago')
g.log.between('tagname1', 'tagname2')
g.log.each {|l| puts l.sha }
g.gblob('v2.5:Makefile').log.since('2 weeks ago')


g.object('HEAD^').to_s  # git show / git rev-parse
g.object('HEAD^').contents
#g.object('v2.5:Makefile').size
#g.object('v2.5:Makefile').sha

#g.gtree(treeish)
#g.gblob(treeish)
#g.gcommit(treeish)

commit = g.gcommit('241d42729774ae1049cc41ee6f38ff042b5b7b21')

commit.gtree
commit.parent.sha
commit.parents.size
commit.author.name
commit.author.email
commit.author.date.strftime("%m-%d-%y")
commit.committer.name
commit.date.strftime("%m-%d-%y")
commit.message

tree = g.gtree("HEAD^{tree}")

tree.blobs
tree.subtrees
tree.children # blobs and subtrees

#g.revparse('v2.5:Makefile')

g.branches # returns Git::Branch objects
g.branches.local
g.branches.remote
g.branches[:master].gcommit
g.branches['origin/master'].gcommit

g.grep('hello')  # implies HEAD
#g.blob('v2.5:Makefile').grep('hello') # undefined method blob
#g.tag('v2.5').grep('hello', 'docs/')

#g.diff(commit1, commit2).size
#g.diff(commit1, commit2).stats
#g.gtree('v2.5').diff('v2.6').insertions
#g.diff('gitsearch1', 'v2.5').path('lib/')
#g.diff('gitsearch1', @git.gtree('v2.5'))
#g.diff('gitsearch1', 'v2.5').path('docs/').patch
#g.gtree('v2.5').diff('v2.6').patch

#g.gtree('v2.5').diff('v2.6').each do |file_diff|
   #puts file_diff.path
   #puts file_diff.patch
   #puts file_diff.blob(:src).contents
#end

g.config('user.name')  # get user name
g.config # returns whole config hash

g.tags # returns array of Git::Tag objects