provider "render" {
  api_key = var.render_api_key
}

resource "render_service" "devops" {
  name        = "devops"
  service_type = "web"
  repo        = "https://github.com/YOUR_USERNAME/hello-devops.git"
  branch      = "main"
  env         = "docker"
  plan        = "free"
}