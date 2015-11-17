{config, "test.conf"}.
{cover, "cover.conf"}.
{alias, test, ".."}.
{suites, test, all}.
{skip_suites, test, [cl_consumer_SUITE, cl_pool_SUITE, cl_queue_SUITE, cl_queue_srv_SUITE], "Skip"}.
{skip_cases, test, cl_dqueue_SUITE, [exports, performance, disk_usage], "Not needed"}.