Got it — you're aiming to **complete all competencies at the "Erweitert (Stufe 3)" level** across all **five phases** of the WordPress migration project (LB2).

Here's a complete, **phase-by-phase step-by-step plan** to reach **full competency** (Stufe 3) in **every single row** of the Bewertungsraster you posted:

---

## ✅ **Phase 1: Planung**

### 1. Projektplan (Stufe 3)

* [ ] Create a **Mermaid Gantt or flow diagram** showing:

  * Milestones (e.g., FTP download, DNS setup, WordPress migration)
  * Phases with individual steps
  * Individual **colors per phase**
* [ ] Add meaningful **milestones** and weekly goals
* [ ] Save in `/01 - Dokumentation/Projektplan.md`

### 2. Architekturdiagramm (Stufe 3)

* [ ] Create a full architecture diagram showing:

  * All components: Webserver, DB server, FTP, DNS
  * **FQDNs**, IPs, and **AWS/EC2 instance names**
  * **Color-coded and labeled** visual structure
* [ ] Export image and include in `/01 - Dokumentation/Architekturdiagramm.png`

---

## ✅ **Phase 2: Umgebung aufbauen**

### 3. Umgebung aufbauen/einrichten (Stufe 3)

* [ ] Build a complete AWS environment based on the architecture:

  * EC2 for Webserver
  * EC2 for DB (separate!)
  * EC2 or Docker container for FTP
  * EC2 or Docker container for DNS
* [ ] Use **SSH keys**, **security groups**, and name each instance clearly (e.g., `web01`, `db01`, `ftp01`)

---

## ✅ **Phase 3: Serverkonfiguration**

### 4. DNS (Stufe 3)

* [ ] Install a **dedicated DNS server** (e.g., `bind9`, `Technitium DNS`)
* [ ] Internally resolve your domain (e.g., `wordpress.lb2.local`)
* [ ] Add proper **A-records** for web and DB servers

### 5. Webserver (Stufe 3)

* [ ] Configure Apache/Nginx:

  * Custom VirtualHost or server block
  * Remove default landing page
  * Setup **HTTP → HTTPS redirect**
* [ ] Use Let's Encrypt or self-signed SSL

### 6. PHP (Stufe 3)

* [ ] Install **PHP-FPM** (e.g., `php8.1-fpm`)
* [ ] Configure Nginx or Apache to use FPM
* [ ] Validate with a `phpinfo.php`

### 7. MySQL/MariaDB (Stufe 3)

* [ ] Install MariaDB/MySQL on a **separate EC2 or container**
* [ ] Create a WordPress user with restricted permissions
* [ ] Only allow access from the Webserver IP
* [ ] Enable SSL between DB and Webserver (optional)

### 8. PhpMyAdmin/Adminer (Stufe 3)

* [ ] Install PhpMyAdmin/Adminer on a **separate host**
* [ ] Enable HTTPS
* [ ] Connect to dedicated DB server
* [ ] Secure with .htpasswd or firewall

### 9. FTP-Server (Stufe 3)

* [ ] Use FTPS (e.g., `vsftpd` or `proftpd`)
* [ ] Generate SSL certificate
* [ ] Configure:

  * User access limited to `DocumentRoot`
  * Encrypted login only (no plain FTP)

---

## ✅ **Phase 4: WordPress Migration**

### 10. WordPress Migration (Stufe 3)

* [ ] Place WordPress files in `DocumentRoot` with correct permissions
* [ ] Modify `wp-config.php` with new DB info
* [ ] Update `WP_HOME` and `WP_SITEURL` **directly in the DB**

```sql
UPDATE wp_options SET option_value='https://yourdomain' WHERE option_name='siteurl';
UPDATE wp_options SET option_value='https://yourdomain' WHERE option_name='home';
```

---

## ✅ **Phase 5: Betrieb & Tools**

### 11. Backup (Stufe 3)

* [ ] Create **CRON jobs**:

  * Daily DB dump (`mysqldump`)
  * File archive (e.g., `tar`)
  * Delete backups older than 7 days
* [ ] Send email notifications via SMTP

  * Use `mail` or `msmtp` in bash script
  * Attach backup log to email

### 12. Testing (Stufe 3)

* [ ] Create a **test catalog** in `/01 - Dokumentation/Testing.md`:

  * 10+ real test cases (login, post, media upload, etc.)
  * Include edge cases and failure handling
* [ ] Ensure no errors in:

  * `/wp-admin/site-health.php`
  * `/wp-admin/admin.php?page=et_support_center_divi`

### 13. Deployment (Stufe 3)

* [ ] Setup **GitHub Actions** (or GitLab CI/CD):

  * Auto-deploy `staging` branch to staging server
  * Auto-deploy `main` branch to live server
* [ ] Confirm both environments work

### 14. Docker (Stufe 3)

* [ ] Dockerize all components:

  * Webserver (Apache/Nginx)
  * PHP-FPM
  * MySQL
  * PhpMyAdmin
  * FTP (vsftpd)
  * DNS (optional: `technitium/dns-server`)
* [ ] Use Docker Compose with **named services** and volumes
* [ ] Place all under `/02 - WordPress/Application/docker-compose.yml`

---

## 📁 **GitHub Repository Structure Reminder**

```
M158-LB2/
├── 01 - Dokumentation/
│   ├── Projektplan.md
│   ├── Architekturdiagramm.png
│   ├── Testing.md
│   └── BackupScript.sh
├── 02 - WordPress/
│   ├── Backup/
│   ├── Application/
│   │   └── docker-compose.yml
│   └── Config/
├── 03 - Diverses/
│   ├── Vorlage Bewertungsraster [DeinName].xlsx
│   └── Logins.txt
```

---

If you want, I can also generate:

* 🧾 Templates for test cases, documentation, backup scripts
* 🐳 Full Docker Compose setup
* 🔧 Systemd timers or CRON templates
* 📬 Bash script for SMTP email with logs

Let me know what you'd like to tackle first.
