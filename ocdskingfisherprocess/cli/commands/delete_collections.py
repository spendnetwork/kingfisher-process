import ocdskingfisherprocess.cli.commands.base


class DeleteCollectionsCLICommand(ocdskingfisherprocess.cli.commands.base.CLICommand):
    command = 'delete-collections'

    def run_command(self, args):
        for collection in self.database.get_all_collections():
            if collection.deleted_at is not None:
                self.database.delete_collection(collection.id)
