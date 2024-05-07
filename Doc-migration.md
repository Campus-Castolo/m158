# Task
We have decided to perform a migration of a WordPress site as described in the module repository. However, we have opted not to use a Proxmox VM provided by TBZ. 
Instead, we are renting a small VPS instance and migrating the website onto it. It is accessible at: firefox.fr.cloud

# Execution

## Setup Database:
![image](https://github.com/Campus-Castolo/m158/assets/125958687/b2983954-f16a-4260-b295-73f2623905a9)

## Database of Origin

Using the [All-in-One WP Migration plugin](https://servmask.com/), we were able to export the entire database as well as all WordPress configurations and settings from the [legacy server](https://m158.geekz.ch/). Using the same plugin, after a standard WordPress installation on the target server, we were able to import the data. In the background, the plugin ensured that the domain of all links was adjusted to match our domain.

### Loading of plugin
![image](https://github.com/Campus-Castolo/m158/assets/125958687/575f464d-4574-43d3-affc-08965b9d93e0)


### Adjustment of .htaccess to fit size of migration
We first adjusted the .htaccess to fit size of migration to this:
![image](https://github.com/Campus-Castolo/m158/assets/125958687/a6ec4005-cae9-4576-867a-2644ef85f127)

Then we noticed that its much more than this, so we adjusted it to this:
![image](https://github.com/Campus-Castolo/m158/assets/125958687/325405c8-9136-4a82-93bd-4334b7bae240)

## Website adjustments
We created the following file to use SSL with our self generated self signed certificates:
![image](https://github.com/Campus-Castolo/m158/assets/125958687/a967c880-e858-469e-b93f-741730a314bc)

## Wordpress Php
We use php 8.1.2

```bash
sudo apt install php8.1.2
sudo apt install php8.1-mysql php8.1-bcmath php8.1-curl php8.1-imagick php8.1-dom php8.1-zip php8.1-intl
a2dismod php8.1
```

![image](https://github.com/Campus-Castolo/m158/assets/125958687/de205256-892d-487e-9ab7-3b385d1d97ab)

## Proof that it works
The website looks identical except that the logo doesn't render.
![image](https://github.com/Campus-Castolo/m158/assets/125958687/8800bc8b-f741-4ea6-ad45-43b117947abf)

## Backup of Site
We used a plugin to make backups as seen in the following screenshit we have made quite many
![image](https://github.com/Campus-Castolo/m158/assets/125958687/dcedb91b-719d-4dee-9eb5-b98fb261900d)

# Aha-moments

## No internet:
We had no internet for a while so we contaced a friend and he helped us solve this, which turned out to be quite simple.

We had to disable the 1 to 1 mapping on the pfsense, which is under Firewall > NAT > 1:1

![image](https://github.com/Campus-Castolo/m158/assets/125958687/c784b308-d882-4ac8-b7bb-bdd1da16ab00)

As seen in the following screen there is no 1:1 mappings any more
