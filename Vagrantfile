# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'yaml'

if File.exists? ('vagrant.yml')
	settings = YAML.load_file 'vagrant.yml'
else
	settings = {}
end

memory = settings['memory'] || 8192
cpus = settings['cpus'] || 4
name = settings['name'] || 'vagrant.bw'

Vagrant.configure(2) do |config|
	config.vm.box = "ubuntu/xenial64"
	config.vm.provider "virtualbox" do |vb|
		#vb.gui = true

		# Number of CPUs
		vb.cpus = cpus

		# Memory
		vb.memory = memory

		# Name in VirtualBox Gui
		vb.name = name
	end
	config.vm.define name
	config.vm.synced_folder './', '/vagrant', type: 'rsync', disabled: true

	# port forwarding
	config.vm.network "forwarded_port", guest: 22, host: 10022, auto_correct: false
	config.vm.network "forwarded_port", guest: 80, host: 10080, auto_correct: false
	config.vm.network "forwarded_port", guest: 443, host: 10443, auto_correct: false
	config.vm.network "forwarded_port", guest: 1883, host: 11883, auto_correct: false

	config.vm.provision "shell", inline: <<-SHELL
	DEBIAN_FRONTEND=noninteractive apt-get update --quiet
	DEBIAN_FRONTEND=noninteractive apt-get upgrade --quiet --yes
	DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes --no-install-recommends \
	file \
	sudo
	DEBIAN_FRONTEND=noninteractive apt-get autoremove --yes 
	DEBIAN_FRONTEND=noninteractive apt-get clean
	SHELL

	config.vm.provision "shell" do |s|
		ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
		s.inline = <<-SHELL
		addgroup --quiet --gid 11000 bborbe 
		adduser --quiet --uid 11000 --gid 11000 --gecos "" --disabled-password --shell /bin/bash bborbe
		mkdir -p /home/bborbe/.ssh
		echo #{ssh_pub_key} > /home/bborbe/.ssh/authorized_keys
		chown -R bborbe /home/bborbe  
		chmod -R go= /home/bborbe     
		echo "bborbe ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/bborbe
		SHELL
	end

end
