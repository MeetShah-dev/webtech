import { HttpService } from '@nestjs/axios';
import { Injectable } from '@nestjs/common';
import { firstValueFrom } from 'rxjs';
import axios from "axios"
import FormData from 'form-data';

@Injectable()
export class SchedulerService {
    constructor(
        private httpService: HttpService
    ) { }

    async getAllUserLikes(req, res) {
        try {
            const response: any = await axios.get(process.env.SOCIAL_API + 'get_all_user_likes', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getAllUserDislikes(req, res) {
        try {
            const response: any = await axios.get(process.env.SOCIAL_API + 'get_all_user_dislikes', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getAllComments(req, res) {
        try {
            const response: any = await axios.get(process.env.SOCIAL_API + 'get_all_comments', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async addComment(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id
        }
        try {
            const response = await firstValueFrom(this.httpService.post(process.env.SOCIAL_API + 'add_comment', payload));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }

    async editComment(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id
        }
        console.log("PAYLOAD--", payload)
        try {
            const response = await firstValueFrom(this.httpService.post(process.env.SOCIAL_API + 'edit_comment', payload));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async updateLikeDislike(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id
        }
        try {
            const response = await firstValueFrom(this.httpService.post(process.env.SOCIAL_API + 'update_like_dislike', payload));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async createSchedule(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id
        }
        try {
            const response = await firstValueFrom(this.httpService.post(process.env.SCHEDULER_API + 'schedule_magazine', payload));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async reSchedule(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id
        }
        try {
            const response = await firstValueFrom(this.httpService.post(process.env.SCHEDULER_API + 'reschedule_magazine', payload));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async getAllMagazine(req, res) {
        try {
            const response: any = await axios.get(process.env.SCHEDULER_API + 'get_all_magazine', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async deleteComment(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id
        }
        console.log("PAYLOAD--", payload)
        try {
            const response = await firstValueFrom(this.httpService.post(process.env.SOCIAL_API + 'delete_comment', payload));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
}



