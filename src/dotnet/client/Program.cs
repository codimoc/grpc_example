
using Grpc.Net.Client;

public class Program
{
    static async Task Main(string[] args)
    {
        using var channel = GrpcChannel.ForAddress("http://localhost:50051");
        var client = new Unary.Unary.UnaryClient(channel);
        var message = new Unary.Message{Message_="Hello from C#"};
        var reply = await client.RespondAsync(message);
        Console.WriteLine(reply);
    }

}

