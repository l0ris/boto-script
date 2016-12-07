from boto.ec2.elb import ELBConnection

from boto.ec2.elb import HealthCheck

conn_elb = ELBConnection(AWS_ACCESS_KEY, AWS_SECRET_KEY)

#For a complete list of options see http://boto.cloudhackers.com/ref/ec2.html#module-boto.ec2.elb.healthcheck
hc = HealthCheck('healthCheck', 
                     interval=10, 
                     target='HTTP:80/index.html',
                     timeout=2)

#For a complete list of options see http://boto.cloudhackers.com/ref/ec2.html#boto.ec2.elb.ELBConnection.create_load_balancer
lb = conn_elb.create_load_balancer('nginx-lb', 
                                       ['eu-central-1', 'eu-west-1'], 
                                       [(80, 80, 'http'), (443, 443, 'tcp')])

lb.configure_health_check(hc)

#DNS name for your new load balancer
print "Map the CNAME of your website to: %s" % (lb.dns_name)
