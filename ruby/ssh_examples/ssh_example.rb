# gem install net-ssh
require 'net/ssh'

# Actually works with prompts
# Kernel.system("ssh -t devdungeon.com bin/backupdate")


Net::SSH.start('devdungeon.com', 'naodano') do |ssh|
    channel = ssh.open_channel do |channel, success|
        channel.on_data do |channel, data|
            puts data.to_s
            if data =~ /^\[sudo\] password for/
                puts "Sending password"
                channel.send_data "secretpassword\n"
            end
            if data =~ /^Enter the letter y to approve/
                channel.send_data "y\n"
            end
        end

        channel.request_pty
        channel.exec("./script_with_prompts")
        channel.wait
      end
      channel.wait
end

