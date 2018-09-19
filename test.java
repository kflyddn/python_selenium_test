public class TestPage2 extends TestCase {
    private Selenium selenium;

    protected void setUp() throws Exception {
       String url = "https://udecide-demo.digitalalchemy.net.au/login";
       selenium = new DefaultSelenium("localhost", SeleniumServer.getDefaultPort(), "*firefox", url);
       selenium.start();
       super.setUp();
    }
    protected void tearDown() throws Exception {
        selenium.stop();
        super.tearDown();
    }
}