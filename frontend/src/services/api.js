export async function getHelloMessage() {
  const res = await fetch("/api/hello/");
  const data = await res.json();
  return data.message;
}
