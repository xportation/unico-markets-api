from markets import storage


def test_just_call_fake_storage_for_coverage():
    fake_storage = storage.FakeStorage()
    fake_storage.add(None)
    fake_storage.flush()
