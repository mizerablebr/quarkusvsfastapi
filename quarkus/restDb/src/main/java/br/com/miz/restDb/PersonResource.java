package br.com.miz.restDb;

import br.com.miz.restDb.domain.Person;

import javax.transaction.Transactional;
import javax.ws.rs.*;
import javax.ws.rs.core.Response;
import java.util.List;

@Path("/person")
public class PersonResource {
    @Transactional
    @POST
    @Consumes("application/json")
    @Produces("application/json")
    public Response add(Person entity) {
        entity.persist();
        return Response.ok(entity).build();
    }

    @GET
    @Produces("application/json")
    @Path("list")
    public Response list() {
        List<Person> people = Person.listAll();
        return Response.ok(people).build();
    }

    @GET
    @Produces("application/json")
    @Path("{name}")
    public Response byName(@PathParam("name") String name) {
        Person person = Person.findByName(name);
        return Response.ok(person).build();
    }
}
