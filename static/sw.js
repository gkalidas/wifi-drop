self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', event => event.waitUntil(self.clients.claim()));

async function notifyClients(data) {
  const all = await self.clients.matchAll({ includeUncontrolled: true });
  for (const client of all) {
    client.postMessage(data);
  }
}

self.addEventListener('backgroundfetchsuccess', event => {
  event.waitUntil(notifyClients({ type: 'BG_FETCH_SUCCESS', id: event.registration.id }));
});

self.addEventListener('backgroundfetchfail', event => {
  event.waitUntil(notifyClients({ type: 'BG_FETCH_FAIL', id: event.registration.id }));
});

self.addEventListener('backgroundfetchabort', event => {
  event.waitUntil(notifyClients({ type: 'BG_FETCH_FAIL', id: event.registration.id }));
});
