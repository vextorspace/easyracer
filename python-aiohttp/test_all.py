import pytest
import aiohttp
import main
from testcontainers.core.generic import DockerContainer
#from testcontainers.core.waiting_utils import wait_container_is_ready


@pytest.mark.asyncio
async def test_all():
    docker_container = DockerContainer("ghcr.io/jamesward/easyracer").with_exposed_ports(8080)
    with docker_container as easyracer:
        port = easyracer.get_exposed_port(8080)

        # todo: can't find the right way to wait on the container being ready
        import time
        time.sleep(2)

        #@wait_container_is_ready()
        async def connected():
            async with aiohttp.ClientSession() as session:
                result1 = await main.scenario1(session, port)
                assert result1 == "right"

                #result2 = await main.scenario2(session, port)
                #assert result2 == "right"

                #result3 = await main.scenario3(session, port)
                #assert result3 == "right"

                #result4 = await main.scenario4(session, port)
                #assert result4 == "right"

                #result5 = await main.scenario5(session, port)
                #assert result5 == "right"

                #result6 = await main.scenario6(session, port)
                #assert result6 == "right"

                result7 = await main.scenario7(session, port)
                assert result7 == "right"

        await connected()