import org.testng.annotations.Test;
import static io.restassured.RestAssured.*;
import org.json.simple.JSONObject;
import java.util.Random;

public class TestApi {
    String url = "https://api.hub.knime.com/repository/Users/foremeka/";
    String bearerToken = " ";
    String spaceName = "space new" + new Random().nextInt();
    @Test
    public void createSpace(){
        JSONObject json = new JSONObject();
        json.put("private", "true");
        json.put("type", "space");
        given().
        headers("Authorization",
                "Bearer " + bearerToken).
        queryParam("overwrite","false").
        contentType("application/json").
        body(json.toJSONString()).
        when().put(url + spaceName).
        then().statusCode(201).
        log().all();
    }
    @Test
    public void deleteSpace() {
        given().
        headers("Authorization",
                "Bearer " + bearerToken).
        when().delete(url + spaceName).
        then().statusCode(204).
        log().all();
    }
}
